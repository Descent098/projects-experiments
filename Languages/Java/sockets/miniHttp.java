import java.net.Socket;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class miniHttp {
    private Socket sock;

    public void initialize(int port) {

        try {
            sock = new Socket("localhost", port);
            System.out.println("Socket created");

            OutputStreamWriter writer = new OutputStreamWriter(sock.getOutputStream());

            BufferedReader reader = new BufferedReader(new InputStreamReader(sock.getInputStream()));
            String message = null;

            writer.write("GET / HTTP/1.1\r\n\r\n");

            while ((message = reader.readLine()) != null) {
                System.out.println("Socket found message");

                System.out.println(message);
            }

            reader.close();

        } catch (Exception e) {
            // TODO: handle exception
        }

    }

    public static void main(String[] args) {
        miniHttp server = new miniHttp();
        try {
            while (true) {
                server.initialize(8118);

            }
        } finally {
            try {
                server.sock.close();
            } catch (Exception e) {
                // TODO: handle exception
            }

        }

    }
}
