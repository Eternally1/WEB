package service;

import java.util.ArrayList;
import java.util.List;

import util.EducateUtil;
import dao.EducateDao;
import entity.Educate;
import entity.EducateString;
import entity.User;

public class EducateService {
	private EducateDao ed=new EducateDao();
	//培养计划录入
	public boolean addEducate(Educate educate){
		  if(!ed.ExistsEducate(educate)){
			  ed.addEducate(educate);
			  System.out.println("添加"+educate.getName()+"成功");
			  return true;
		  }
		return false;
		
	}
	//培训计划查看
	public List<EducateString>   listEducate(){
		List<Educate> list=ed.listEducate();
		List<EducateString> listRes = new ArrayList<EducateString>();
		for(Educate ed:list){
			EducateString eds=new EducateString();
			EducateUtil.setEducateString(ed, eds);
			listRes.add(eds);
		}
		System.out.println("列举成功");
		return listRes;
	}
	//培训详情
	public EducateString detailEducate(Long id){
		Educate edu=ed.loadEducate(id);
		EducateString eds=new EducateString();
		EducateUtil.setEducateString(edu, eds);
		System.out.println("培训详情---");
		return eds;
	}
	//删除培训
	public void deleteEducate(Educate educate){
	   ed.deleteEducate(educate);
	   System.out.print("删除培训信息成功");
	}
}
