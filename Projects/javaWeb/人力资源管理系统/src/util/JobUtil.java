package util;

import java.util.Date;

import entity.Job;
import entity.JobString;

public class JobUtil {
	public static void setJob(Job job,JobString jobs){
		//Long idd=Long.parseUnsignedLong(jobs.getId().trim());
		//job.setId(idd);
		job.setName(jobs.getName());
		Byte sex=Byte.parseByte(jobs.getSex().trim());
		job.setSex(sex);
		if(!jobs.getAge().equals("")){
		   Integer age=Integer.parseInt(jobs.getAge().trim());
		   job.setAge(age);
		}
		job.setSpecialty(jobs.getSpecialty());
		job.setExperience(jobs.getExperience());
		job.setStudyeffort(jobs.getStudyeffort());
		job.setSchool(jobs.getSchool());
		job.setJob(jobs.getJob().trim());
		job.setTel(jobs.getTel());
		job.setEmail(jobs.getEmail());
		//Date createtime = DateUtil.parseToDate(jobs.getCreatetime().trim(), DateUtil.yyyyMMdd);
		//job.setCreatetime(createtime);
		job.setContent(jobs.getContent());
		//Byte isstock=Byte.parseByte(jobs.getIsstock().trim());
		//job.setIsstock(isstock);
	}
	public static void setJobId(Job job,JobString jobs){
		Long idd=Long.parseLong(jobs.getId().trim());
		job.setId(idd);
	}
   /* public static void setJobString(Job job,JobString jobs){
    	jobs.setId(job.getId().toString());
    	jobs.setName(job.getName().trim());
    	jobs.setSex(job.getSex().toString());
    	jobs.setAge(job.getAge().toString());
    	jobs.setJob(job.getJob().trim());
    	jobs.setSpecialty(job.getSpecialty().trim());
    	if(job.getContent()!=null){
    	    jobs.setContent(job.getContent());
    	 }
    	jobs.setTel(job.getTel().trim());
    }*/
}
