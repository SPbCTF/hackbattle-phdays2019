package spbctf;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.VBox;
import javafx.scene.text.TextAlignment;
import javafx.stage.Stage;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
//import phd.2019.spbctf;


public class Main extends Application {

    Stage  mainWindow;

    @Override
    public void start(Stage primaryStage) throws Exception{

        mainWindow = primaryStage;
        mainWindow.setTitle("mDs");
        mainWindow.setResizable(false);

        GridPane gridPane = new GridPane();
        gridPane.setPadding(new Insets(10, 10,10,10));
        gridPane.setVgap(10);
        gridPane.setHgap(12);

        Label inputStringLabel = new Label("Говори пароль");
        GridPane.setConstraints(inputStringLabel, 0,0);

        TextField inputString = new TextField();
        inputString.setMinWidth(340);
        GridPane.setConstraints(inputString,1,0);

        Label infoLabel = new Label("Они говорили: \"Нужны сложные пароли! Секурити! Бла бла бла!\" Ну вот держите. 10 слов разделенных пробелом. Слабо похакать?");
        GridPane.setConstraints(infoLabel, 1,3);
        infoLabel.setWrapText(true);
        infoLabel.setMaxWidth(470);
        infoLabel.setAlignment(Pos.CENTER);
        infoLabel.setTextAlignment(TextAlignment.CENTER);

        Button inputButton = new Button("Говорю пароль");

        inputButton.setOnAction(e -> {

            String[] arrOfStr = inputString.getText().split(" ");
            int words =  arrOfStr.length;
            if (words == 10) {
                try {
                    if ((getmd5(arrOfStr[6]).equals("dd7536794b63bf90eccfd37f9b147d7f")) && (getmd5md5(arrOfStr[2]).equals("ecf82c75bf5ac5008a7757c14247b8d7")) && (getsha_512(arrOfStr[8]).equals("9060148b9a76b89faab87558c33ee1eaaad6db30f58788b8be994347b6acc62962c949a634294206547d64b3d79e791f32e1547e98d4b94463d52eac3b1c9b00"))) {
                        if ((getsha_256(arrOfStr[5]).equals("a511aeeeb8a119931a67038a63b7974faee48712de1c79391ebe2c9b929678e9")) && (getsha_1(arrOfStr[3]).equals("cffa50a32cb13a240d705317bcec65dd1f31b6ad"))) {
                            if ((getsha_384(arrOfStr[4]).equals("7f4cb2ea018f770ac03738d8abfdae023e6e368a0a3440d126a557c4d0c2a00efafccf4b691cb76ce6bdf8887db3ba84")) && (getsha_512(arrOfStr[1]).equals("60e00ebd283eacdcea353a2f943e57abe04406cf8506413224d55f270b255c60c2d0d3b62e1c63181f2affc2a264ae9196feda06518ff087aee76e9582a28662")) && (getsha_224(arrOfStr[0]).equals("ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193"))) {
                                if ((getmd5md5(arrOfStr[7]).equals("bf025b4ee66e0aa85489cca4533d3dd0")) && (getsha_384(arrOfStr[9]).equals("a8b64babd0aca91a59bdbb7761b421d4f2bb38280d3a75ba0f21f2bebc45583d446c598660c94ce680c47d19c30783a7"))) {
                                    int[] flag_enc = {62,57,61,59,68,75,113,77,54,86,59,99,141,64,135,110,78,56,143,129,94,56,72};
                                    String key = "";
                                    for (String a : arrOfStr)
                                        key+=a;
                                    infoLabel.setText(decrypt(flag_enc,key));
                                }
                                else {
                                    infoLabel.setText("ООООО, ты зашел таааааак далекооо... Еще чуть-чуть...");
                                }
                            }
                            else {
                                infoLabel.setText("Ого! это ведь прав... а нет, не правильный пароль.");
                            }
                        }
                        else {
                            infoLabel.setText("Мне кажется, ты меня обманываешь...");
                        }
                    }
                    else {
                        infoLabel.setText("Ты дурак, и пароль твой дурацкий!");
                    }
                }
                catch (NoSuchAlgorithmException ex)
                {
                    ex.printStackTrace();
                }
            }
            else {
                if (words < 10) {
                    infoLabel.setText("Такой маленький пароль? Ой, а разговоров то было...");
                }
                if (words > 10) {
                    infoLabel.setText("Не, ну это уже Эребор... Сказано же - 10. Десять.");
                }
            }
        });
        GridPane.setConstraints(inputButton,1,2);
        gridPane.getChildren().addAll(inputStringLabel, inputString, inputButton);
        VBox mainLayout = new VBox();
        mainLayout.getChildren().addAll(gridPane, infoLabel);
        Scene scene = new Scene(mainLayout, 470, 140);
        mainWindow.setScene(scene);
        mainWindow.show();
    }

    public static void main(String[] args) {
        launch(args);
    }

    public String getmd5(String data) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(data.getBytes());
        byte[] digest = md.digest();
        StringBuffer sb = new StringBuffer();
        for (byte b : digest) {
            sb.append(String.format("%02x", b & 0xff));
        }
        return sb.toString();
    }

    public String getmd5md5(String data) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(data.getBytes());
        byte[] digest = md.digest();
        StringBuffer sb = new StringBuffer();
        for (byte b : digest) {
            sb.append(String.format("%02x", b & 0xff));
        }

        md.update(sb.toString().getBytes());
        digest = md.digest();
        sb = new StringBuffer();
        for (byte b : digest) {
            sb.append(String.format("%02x", b & 0xff));
        }
        return sb.toString();
    }

    public String getsha_256(String data) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(data.getBytes());
        byte[] digest = md.digest();
        StringBuffer spbctf = new StringBuffer();
        for (byte b : digest) {
            spbctf.append(String.format("%02x", b & 0xff));
        }
        return spbctf.toString();
    }

    public String getsha_1(String data) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-1");
        md.update(data.getBytes());
        byte[] digest = md.digest();
        StringBuffer sb = new StringBuffer();
        for (byte b : digest) {
            sb.append(String.format("%02x", b & 0xff));
        }
        return sb.toString();
    }

    public String getsha_384(String data) throws NoSuchAlgorithmException {
        //Security.addProvider(new Bounc)
        MessageDigest md = MessageDigest.getInstance("SHA-384");
        md.update(data.getBytes());
        byte[] digest = md.digest();
        StringBuffer sb = new StringBuffer();
        for (byte b : digest) {
            sb.append(String.format("%02x", b & 0xff));
        }
        return sb.toString();
    }

    public String getsha_512(String data) throws NoSuchAlgorithmException {
        //Security.addProvider(new Bounc)
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        md.update(data.getBytes());
        byte[] digest = md.digest();
        StringBuffer spbctf = new StringBuffer();
        for (byte b : digest) {
            spbctf.append(String.format("%02x", b & 0xff));
        }
        return spbctf.toString();
    }

    public String getsha_224(String data) throws NoSuchAlgorithmException {
        //Security.addProvider(new Bounc)
        MessageDigest md = MessageDigest.getInstance("SHA-224");
        md.update(data.getBytes());
        byte[] digest = md.digest();
        StringBuffer sb = new StringBuffer();
        for (byte b : digest) {
            sb.append(String.format("%02x", b & 0xff));
        }
        return sb.toString();
    }

    private static int[] encrypt(String str, String key) {
        int[] output = new int[str.length()];
        for(int i = 0; i < str.length(); i++) {
            int o = (Integer.valueOf(str.charAt(i)) ^ Integer.valueOf(key.charAt(i % (key.length() - 1)))) + '0';
            output[i] = o;
        }
        return output;
    }

    private static String decrypt(int[] input, String key) {
        String output = "";
        for(int i = 0; i < input.length; i++) {
            output += (char) ((input[i] - 48) ^ (int) key.charAt(i % (key.length() - 1)));
        }
        return output;
    }
}
