package server;

import common.HelloWorldClient;
import common.HelloWorldServer;

import java.io.*;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;


public class HelloWorldImplementation extends UnicastRemoteObject implements HelloWorldServer {
    private boolean started = false;
    private boolean end = false;
    private String [][] quests;
    private ArrayList<HelloWorldClient> clients = new ArrayList<HelloWorldClient>();
    private HashMap<String,Integer[]> grade = new HashMap<String,Integer[]>();//ID,QUEST,POINTS
    private Request requester = new Request();
    private String id_exam = new String();
    private String location = new String();
    public HelloWorldImplementation() throws RemoteException {
        try {
            PrepareExam();
        } catch (Exception e) {
            e.printStackTrace();
        }
        quests = new String[3][5];
        String csvFile = "resources/test.csv";
        BufferedReader br = null;
        String line = "";
        String cvsSplitBy = ";";
        Integer index = 0;
        try {
            br = new BufferedReader(new FileReader(csvFile));
            while ((line = br.readLine()) != null) {
                // use comma as separator
                String[] lineSplit = line.split(cvsSplitBy);
                String sendQuestion = "{\"id_exam\": "+id_exam+",\"question\":\""+lineSplit[0]+"\", \"answer1\": \""+lineSplit[1]+"\", \"answer2\": \""+lineSplit[2]+"\", \"answer3\": \""+lineSplit[3]+"\", \"correct_answer\": \""+lineSplit[4]+"\"}";
                requester.post("http://127.0.0.1:5000/question/1", sendQuestion);
                quests[index] = lineSplit;
                index++;
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
    private void PrepareExam() throws Exception{
        String separator = "\\\\";
        String info = "{\"description\": \"Maths\",\"date\":\"01/01/2021\", \"time\": \"120\", \"location\": \"Port:5000,Host:http://127.0.0.1\"}";
        requester.post("http://127.0.0.1:5000/exams/", info);
        String returned = requester.get("http://127.0.0.1:5000/examslast/Maths").replace(separator,"");
        List<String> listreturned = new ArrayList<String>(Arrays.asList(returned.replace(",","").split(" ")));
        id_exam =  listreturned.get(1);
        location = listreturned.get(listreturned.size() - 1).replace("\"","").split("}")[0];
    }


    public void register(HelloWorldClient client) throws RemoteException {
        if (!started) {
            this.grade.put(client.notifyRegist(), new Integer[]{0,0});
            this.clients.add(client);
            System.out.println("Registering Student, Nº registered students: "+clients.size());
        }else{
            client.notifyExamStarted();
        }
    }
    public void startExam() throws RemoteException{
        started = true;
        notify_StartExam();
    }

    @Override
    public void endExam() throws RemoteException {
        synchronized(this) {
            end = true;
        }
        try (PrintWriter writer = new PrintWriter(new File("resources/grade.csv"))) {

            StringBuilder sb = new StringBuilder();
            sb.append("UniversityID");
            sb.append(';');
            sb.append("Answers");
            sb.append(';');
            sb.append("Correct");
            sb.append('\n');
            for (String name: grade.keySet()){
                Integer[] results = grade.get(name);
                sb.append(name);
                sb.append(';');
                sb.append(results[0]);
                sb.append(';');
                sb.append(results[1]);
                sb.append('\n');
            }
            writer.write(sb.toString());

        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        }
    }

    public void notify_StartExam() throws RemoteException{
        for (HelloWorldClient client : clients){
            new Thread("" + client.getID()){
                public void run(){
                    while(grade.get(client.getID())[0] != quests.length && !end) {
                        try {
                            sendAnswer(client.getID(), client.notifyStartExam(getQuest(client.getID())));
                        } catch (RemoteException e) {
                            e.printStackTrace();
                        }
                    }
                    try {
                        client.notifyGrade(client.getID()+" note: "+grade.get(client.getID())[1]+"/"+quests.length);
                    } catch (RemoteException e) {
                        e.printStackTrace();
                    }
                }
            }.start();
            }
    }
    public String[] getQuest(String id)throws RemoteException{
        Integer[] quest = this.grade.get(id);
        String[] pregunta = Arrays.copyOfRange(this.quests[quest[0]],0,4);
        return pregunta;
    }
    public void sendAnswer(String id, Integer resp)throws RemoteException{
        Integer[] quest = this.grade.get(id);
        if (this.quests[quest[0]][4].equals(resp.toString()) && !end){
            quest[1]++;
        }
        quest[0]++;
        this.grade.put(id, quest);

    }
}
