import java.util.*; //temporary until I know what I need

public class Main{

  public static void main(String[] args) {
    System.out.println("=====Welcome to Werewolf=====");
    Player test = new Player("Tom", 4);
    ArrayList<Integer> roles = createRoleList(10);
    System.out.println(roles);
    System.out.println(test.getName() + " " + test.getRole());

  }

  public static ArrayList<Integer> createRoleList(int numofPlayers){
    ArrayList<Integer> playerRoles = new ArrayList<>();
    Random r = new Random();
    int q;
    for(int l = 1; l == 100; l++){
      System.out.println("Hello");

      q = r.nextInt(5);
      q = new Integer(q);
      playerRoles.add(q);
      System.out.println(q);
    }
      //System.out.println(l);

    System.out.println(playerRoles);
    return playerRoles;
  }

}
