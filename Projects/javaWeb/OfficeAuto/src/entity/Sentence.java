package entity;

import java.io.Serializable;

public class Sentence implements Serializable{
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private int id;
	private String sent;
	
	public Sentence(){};
	public String getSent() {
		return sent;
	}
	public void setSent(String sent) {
		this.sent = sent;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
}
