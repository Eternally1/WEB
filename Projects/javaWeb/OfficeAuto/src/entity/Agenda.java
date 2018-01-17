package entity;
import java.util.Date;

public class Agenda {
	private int id;//日程编号
	private Date starttime;//开始时间
	private Date endtime;//截止时间
	private String content;//日程内容
	private int state;//日程状态
	private String userID;//用户ID
	//这些属性不在数据库中	
	private String begintime;//开始时间
	private String finishtime;//结束时间
	
	
	public Agenda() {}
	

	public String getBegintime() {
		return begintime;
	}
	public void setBegintime(String begintime) {
		this.begintime = begintime;
	}
	public String getFinishtime() {
		return finishtime;
	}
	public void setFinishtime(String finishtime) {
		this.finishtime = finishtime;
	}

	public String getUserID() {
		return userID;
	}
	public void setUserID(String userID) {
		this.userID = userID;
	}
	//日程编号
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	//开始时间
	public Date getStarttime() {
		return starttime;
	}
	public void setStarttime(Date starttime) {
		this.starttime = starttime;
	}
	
	//截止时间
	public Date getEndtime() {
		return endtime;
	}
	public void setEndtime(Date endtime) {
		this.endtime = endtime;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	//日程状态
	public int getState() {
		return state;
	}
	public void setState(int state) {
		this.state = state;
	}
}
