import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.net.URL;

class Rest_server_test {
    private static Request consultor;
    @BeforeAll
    static void beforeAll() {
        consultor = new Request();
    }

    @Test
    void ListExams() throws Exception {
        //GET
        String expected = "[{\"id_exam\": 1, \"description\": \"description1\", \"date\": \"01/01/2021\", \"time\": \"120\", \"location\": \"UdL\"}, {\"id_exam\": 2, \"description\": \"description1\", \"date\": \"01/01/2021\", \"time\": \"120\", \"location\": \"UdL\"}, {\"id_exam\": 3, \"description\": \"description3\", \"date\": \"01/01/2021\", \"time\": \"120\", \"location\": \"UdL\"}]";
        assertEquals(expected, consultor.get("http://127.0.0.1:5000/exams/"));
    }
    @Test
    void ListExam1() throws Exception {
        //GET
        String expected = "[{\"id_exam\": 1, \"description\": \"description1\", \"date\": \"01/01/2021\", \"time\": \"120\", \"location\": \"UdL\"}]";
        assertEquals(expected, consultor.get("http://127.0.0.1:5000/exams/1"));
    }
    @Test
    void AddExam() throws Exception {
        //POST
        String expected = "{\"description\": \"description3\",\"date\":\"01/01/2021\", \"time\": \"120\", \"location\": \"UdL\"}";
        assertEquals("1 record inserted", consultor.post("http://127.0.0.1:5000/exams/", expected));
    }

    @Test
    void AddQuestion() throws Exception {
        //POST
        String expected = "{\"id_exam\": 1,\"question\":\"34+1\", \"answer1\": \"35\", \"answer2\": \"10\", \"answer3\": \"20\", \"correct_answer\": \"1\"}";
        assertEquals("\"1 record inserted\"", consultor.post("http://127.0.0.1:5000/question/1", expected));
    }

}