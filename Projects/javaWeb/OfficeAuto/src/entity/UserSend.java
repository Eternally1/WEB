package entity;

public class UserSend {
	private String username;
	private int role;
	private String userID;
	private int gender;
	
	public int getGender() {
		return gender;
	}
	public void setGender(int gender) {
		this.gender = gender;
	}
	public UserSend() {}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public int getRole() {
		return role;
	}
	public void setRole(int role) {
		this.role = role;
	}
	
	public String getUserID() {
		return userID;
	}
	public void setUserID(String userID) {
		this.userID = userID;
	}
	public UserSend(String username, int role,String userID,int gender) {
		super();
		this.username = username;
		this.role = role;
		this.userID = userID;
		this.gender=gender;
	}
	

}
