package Client;
import common.HelloWorldClient;
import common.HelloWorldServer;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {
    public static void main(String[] args) {
        String host = (args.length < 1) ? null : args[0];
        try {
            Registry registry = LocateRegistry.getRegistry(host);
            HelloWorldClient client = new HelloWorldClientImpl();
            HelloWorldServer stub = (HelloWorldServer) registry.lookup("Hello");
            stub.register(client);
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString()); e.printStackTrace();
        }
    }
}

