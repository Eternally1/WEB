package entity;

import java.util.Date;

public class User {
	private String id;           	//员工编号
	private String username;	//员工用户名
	private String password;	//登录密码
	private String  sex;			//性别
	private String  birthday;		//生日
	private String createtime;	//创建时间
	private String isadmin;		//是否为管理员
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getSex() {
		return sex;
	}
	public void setSex(String sex) {
		this.sex = sex;
	}
	public String getBirthday() {
		return birthday;
	}
	public void setBirthday(String birthday) {
		this.birthday = birthday;
	}
	public String getCreatetime() {
		return createtime;
	}
	public void setCreatetime(String createtime) {
		this.createtime = createtime;
	}
	public String getIsadmin() {
		return isadmin;
	}
	public void setIsadmin(String isadmin) {
		this.isadmin = isadmin;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	private String content;		//人员简介
}
