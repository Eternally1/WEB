package action;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import service.EducateService;
import util.EducateUtil;
import util.JobUtil;
import util.MapUtil;
import util.actionUtil;

import com.opensymphony.xwork2.ActionSupport;
import com.opensymphony.xwork2.ModelDriven;

import entity.Educate;
import entity.EducateString;
import entity.Job;

public class educateAction extends ActionSupport implements ModelDriven<EducateString> {
	private EducateString eds=new EducateString();
	private Map<String,Object> educateAction= new HashMap<String, Object>();
	private EducateService educateService=new EducateService();
    //培养计划录入
	public String addEducate(){
		String  flag="";
		educateAction.clear();
		actionUtil.kuayu();
		Educate educate=new Educate();
		EducateUtil.setEducate(educate, eds);
		if(educateService.addEducate(educate)){
			MapUtil.setStatus(educateAction, "1002");
			MapUtil.setOther(educateAction, "添加培养计划成功");
			flag="success";
		}else{
			MapUtil.setStatus(educateAction, "1001");
			MapUtil.setOther(educateAction, "添加培养计划失败,已存在");
			flag="failed";
		}
		return flag;
		
	}
	//培训计划查看
	public String listEducate(){
		educateAction.clear();
		actionUtil.kuayu();
		List<EducateString>  list=educateService.listEducate();
		MapUtil.setStatus(educateAction, "1002");
		MapUtil.setOther(educateAction, list);
		MapUtil.setTotalNumber(educateAction, list.size());
		return "success";
	}
	//培训详情
	public String detailEducate(){
		educateAction.clear();
		actionUtil.kuayu();
		Long idd=Long.parseLong(eds.getId().trim());
		EducateString  edst=educateService.detailEducate(idd);
		MapUtil.setStatus(educateAction, "1002");
		MapUtil.setOther(educateAction, edst);
		return "success";
	}
	//培训删除
	public String deleteEducate(){
		actionUtil.kuayu();
		educateAction.clear();
		Educate edu=new Educate();
		EducateUtil.setEducateId(edu, eds);
		educateService.deleteEducate(edu);
		MapUtil.setStatus(educateAction, "1002");//删除成功
		MapUtil.setOther(educateAction, "删除成功");
		return "success";
	}
	@Override
	public EducateString getModel() {
		return eds;
	}
	public Map<String, Object> getEducateAction() {
		return educateAction;
	}
  
}
