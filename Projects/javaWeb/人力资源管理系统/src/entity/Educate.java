package entity;

import java.io.Serializable;
import java.util.Date;

/**
 * 培训信息类
 * @author 董元杰
 *
 */
public class Educate implements Serializable{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private Long id;		//培训编号
	private String name;	//培训名称
	private String purpose;	//培训目的
	private Date begintime;	//培训开始时间
	private Date endtime;	//培训结束时间
	private String datum;	//培训材料
	private String teacher;	//培训讲师
	private String student;	//培训人员
	private Date createtime;//创建时间
	private Byte educate;	//培训是否完成
	private String effect;	//培训效果
	private String summarize;//总结
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
	public String getPurpose() {
		return purpose;
	}
	public void setPurpose(String purpose) {
		this.purpose = purpose;
	}
	public Date getBegintime() {
		return begintime;
	}
	public void setBegintime(Date begintime) {
		this.begintime = begintime;
	}
	public Date getEndtime() {
		return endtime;
	}
	public void setEndtime(Date endtime) {
		this.endtime = endtime;
	}
	public String getDatum() {
		return datum;
	}
	public void setDatum(String datum) {
		this.datum = datum;
	}
	public String getTeacher() {
		return teacher;
	}
	public void setTeacher(String teacher) {
		this.teacher = teacher;
	}
	public String getStudent() {
		return student;
	}
	public void setStudent(String student) {
		this.student = student;
	}
	public Date getCreatetime() {
		return createtime;
	}
	public void setCreatetime(Date createtime) {
		this.createtime = createtime;
	}
	public Byte getEducate() {
		return educate;
	}
	public void setEducate(Byte educate) {
		this.educate = educate;
	}
	public String getEffect() {
		return effect;
	}
	public void setEffect(String effect) {
		this.effect = effect;
	}
	public String getSummarize() {
		return summarize;
	}
	public void setSummarize(String summarize) {
		this.summarize = summarize;
	}
	@Override
	public String toString() {
		return "Educate [id=" + id + ", name=" + name + ", purpose=" + purpose
				+ ", begintime=" + begintime + ", endtime=" + endtime
				+ ", datum=" + datum + ", teacher=" + teacher + ", student="
				+ student + ", createtime=" + createtime + ", educate="
				+ educate + ", effect=" + effect + ", summarize=" + summarize
				+ "]";
	}
	
}
