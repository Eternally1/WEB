package entity;

import java.io.Serializable;
import java.util.Date;

/**
 * 应聘人员信息类
 * @author 董元杰
 *
 */
public class Job implements Serializable{
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private Long id;		//应聘人员编号
	private String name;	//姓名
	private Byte sex;		//性别
	private Integer age;	//年龄
	private String job;		//职位
	private String specialty;//所学专业
	private String experience;//工作经验
	private String studyeffort;//学历
	private String school;	//毕业学校
	private String tel;		//电话
	private String email;	//email地址
	private Date createtime;//创建时间
	private String content;	//详细经历
	private Byte isstock;	//是否入库
	public Long getId() {
		return id;
	}
	public void setId(Long id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Byte getSex() {
		return sex;
	}
	public void setSex(Byte sex) {
		this.sex = sex;
	}
	public Integer getAge() {
		return age;
	}
	public void setAge(Integer age) {
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
	public Date getCreatetime() {
		return createtime;
	}
	public void setCreatetime(Date createtime) {
		this.createtime = createtime;
	}
	public String getContent() {
		return content;
	}
	public void setContent(String content) {
		this.content = content;
	}
	public Byte getIsstock() {
		return isstock;
	}
	public void setIsstock(Byte isstock) {
		this.isstock = isstock;
	}
	@Override
	public String toString() {
		return "Job [id=" + id + ", name=" + name + ", sex=" + sex + ", age="
				+ age + ", job=" + job + ", specialty=" + specialty
				+ ", experience=" + experience + ", studyeffort=" + studyeffort
				+ ", school=" + school + ", tel=" + tel + ", email=" + email
				+ ", createtime=" + createtime + ", content=" + content
				+ ", isstock=" + isstock + "]";
	}
	
}
