package entity;

import java.io.Serializable;
import java.util.Date;

public class Diary implements Serializable{
	/**
	 * 工作日志
	 */
	private static final long serialVersionUID = 1L;
	private int id;
	private Date time;//发布时间
	private String content;//日志内容
	private String title;//日志标题
	private String userID;//所属用户
	private String strTime;

	public Diary() {}
	public String getStrTime() {
		return strTime;
	}
	public void setStrTime(String strTime) {
		this.strTime = strTime;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	//发布时间
	public Date getTime() {
		return time;
	}
	public void setTime(Date time) {
		this.time = time;
	}
	
	//日志内容
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	
	//日志标题
	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}
	//所属用户
	public String getUserID() {
		return userID;
	}
	public void setUserID(String userID) {
		this.userID = userID;
	}
	
	@Override
	public String toString() {
		return "Diary [id=" + id + ", time=" + time + ", content=" + content
				+ ", title=" + title + ", userID=" + userID 
				+ "]";
	}	
}
