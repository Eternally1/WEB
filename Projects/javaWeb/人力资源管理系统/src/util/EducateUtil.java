package util;

import java.util.Date;

import entity.Educate;
import entity.EducateString;
import entity.Job;
import entity.JobString;

public class EducateUtil {
	public static void setEducate(Educate educate,EducateString eds){
		educate.setName(eds.getName().trim());
		educate.setPurpose(eds.getPurpose().trim());
		if(!eds.getBegintime().equals("") && !eds.getEndtime().equals("")){//开始和结束必须同时有
		   Date begintime = DateUtil.parseToDate(eds.getBegintime().trim(), DateUtil.yyyyMMdd);
		   educate.setBegintime(begintime);
		   Date endtime = DateUtil.parseToDate(eds.getEndtime().trim(), DateUtil.yyyyMMdd);
		   educate.setEndtime(endtime);
		}
		educate.setDatum(eds.getDatum().trim());
		educate.setTeacher(eds.getTeacher().trim());
		educate.setStudent(eds.getStudent());
		//Date createtime= DateUtil.parseToDate(eds.getCreatetime().trim(), DateUtil.yyyyMMdd);
		//educate.setCreatetime(createtime);
		if(!eds.getEducate().equals("")){
		   Byte educate1=Byte.parseByte(eds.getEducate().trim());
		   educate.setEducate(educate1);
		}
		if(!eds.getEffect().equals("")){
		   educate.setEffect(eds.getEffect().trim());
		}
		if(!eds.getSummarize().equals("")){
		   educate.setSummarize(eds.getSummarize());
		}
	}
	public static void setEducateId(Educate educate,EducateString eds){
		Long idd=Long.parseLong(eds.getId().trim());
		educate.setId(idd);
	}
	
	public static void setEducateString(Educate educate,EducateString eds){
		eds.setId(educate.getId().toString().trim());
		eds.setName(educate.getName().toString().trim());
		eds.setPurpose(educate.getPurpose());
		eds.setEffect(educate.getEffect());
		eds.setDatum(educate.getDatum());
		eds.setTeacher(educate.getTeacher());
		eds.setStudent(educate.getStudent());
		eds.setEffect(educate.getEffect());
		eds.setSummarize(educate.getSummarize());
		eds.setEducate(educate.getEducate().toString());
		if(!educate.getBegintime().equals("")){
			String begintime = DateUtil.parseToString(educate.getBegintime(), DateUtil.yyyyMMdd);
			eds.setBegintime(begintime);
		}
		if(!educate.getEndtime().equals("")){
			String endtime = DateUtil.parseToString(educate.getEndtime(), DateUtil.yyyyMMdd);
			eds.setEndtime(endtime);
		}
	}

}
