package entity;

import java.io.Serializable;
import java.util.Date;

/**
 * 人员信息类
 * @author 董元杰
 *
 */
public class Users implements Serializable{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private Long id;           	//员工编号
	private String username;	//员工用户名
	private String password;	//登录密码
	private Byte sex;			//性别
	private Date birthday;		//生日
	private Date createtime;	//创建时间
	private Byte isadmin;		//是否为管理员
	private String content;		//人员简介
	public Long getId() {
		return id;
	}
	public void setId(Long id) {
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
	public Byte getSex() {
		return sex;
	}
	public void setSex(Byte sex) {
		this.sex = sex;
	}
	public Date getBirthday() {
		return birthday;
	}
	public void setBirthday(Date birthday) {
		this.birthday = birthday;
	}
	public Date getCreatetime() {
		return createtime;
	}
	public void setCreatetime(Date createtime) {
		this.createtime = createtime;
	}
	public Byte getIsadmin() {
		return isadmin;
	}
	public void setIsadmin(Byte isadmin) {
		this.isadmin = isadmin;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	@Override
	public String toString() {
		return "Users [id=" + id + ", username=" + username + ", password="
				+ password + ", sex=" + sex + ", birthday=" + birthday
				+ ", createtime=" + createtime + ", isadmin=" + isadmin
				+ ", content=" + content + "]";
	}
	
}
