package entity;

import java.util.Date;

public class JobString {
	private String id;		//应聘人员编号
	private String name;	//姓名
	private String sex;		//性别
	private String age;	//年龄
	private String job;		//职位
	private String specialty;//所学专业
	private String experience;//工作经验
	private String studyeffort;//学历
	private String school;	//毕业学校
	private String tel;		//电话
	private String email;	//email地址
	private String createtime;//创建时间
	private String content;	//详细经历
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getSex() {
		return sex;
	}
	public void setSex(String sex) {
		this.sex = sex;
	}
	public String getAge() {
		return age;
	}
	public void setAge(String age) {
		this.age = age;
	}
	public String getJob() {
		return job;
	}
	public void setJob(String job) {
		this.job = job;
	}
	public String getSpecialty() {
		return specialty;
	}
	public void setSpecialty(String specialty) {
		this.specialty = specialty;
	}
	public String getExperience() {
		return experience;
	}
	public void setExperience(String experience) {
		this.experience = experience;
	}
	public String getStudyeffort() {
		return studyeffort;
	}
	public void setStudyeffort(String studyeffort) {
		this.studyeffort = studyeffort;
	}
	public String getSchool() {
		return school;
	}
	public void setSchool(String school) {
		this.school = school;
	}
	public String getTel() {
		return tel;
	}
	public void setTel(String tel) {
		this.tel = tel;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getCreatetime() {
		return createtime;
	}
	public void setCreatetime(String createtime) {
		this.createtime = createtime;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	public String getIsstock() {
		return isstock;
	}
	public void setIsstock(String isstock) {
		this.isstock = isstock;
	}
	private String isstock;	//是否入库
}
