public class Player{
  private String name;
  private int playerNumber;
  private int nightsSurvived;
  private int roleID; //Set on game setup; determines role
  private String affinity; //What team the player is on; town, wolves etc.
  private String type;//is the player a blocker, protector etc. determined by role


  /** Default constructor*/
  Player(){
    System.out.println("Not all variables set");
  }

  Player(String Name, int roleNum){
    name = Name;
    roleID = roleNum;
    System.out.println("Name set to: " + name + "Role set to" + getRole());
  }



  public String getRole(){
    //switch roleID //Need to fill in
    System.out.println(roleID);
    switch(roleID){
      case 1: return "Wolf";

      case 2: return "Wolfcub";

      case 3: return "Bodyguard";

      case 4: return "Seer";

    }
    return "Error has occured, bad boi put an int in for a char";
  }

  public String getName(){
    String nn = new String(name); //keeping things encapsulated
    return nn;
  }

}
