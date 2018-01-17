package action;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpServletResponse;

import org.apache.struts2.ServletActionContext;

import service.JobService;
import util.JobUtil;
import util.MapUtil;
import util.actionUtil;

import com.opensymphony.xwork2.ActionSupport;
import com.opensymphony.xwork2.ModelDriven;

import entity.Job;
import entity.JobString;

public class JobAction extends ActionSupport  implements ModelDriven<JobString>{
	
	private  JobString jobs=new JobString();
	private JobService js=new JobService();
	private Map<String,Object> jobAction= new HashMap<String, Object>();
	//添加应聘信息
	public String addJob(){
		actionUtil.kuayu();
		String flag="";
		Job job=new Job();
		JobUtil.setJob(job, jobs);
	    if(js.addJob(job)){
		  MapUtil.setStatus(jobAction, "1002");
		  MapUtil.setOther(jobAction, "添加应聘信息成功");
		  flag="success";
	    }else{
	       MapUtil.setStatus(jobAction, "1001");
	       MapUtil.setOther(jobAction, "用户已存在");
	       flag="failed";
	    }
	    return flag;
	}
  //列举所有应聘信息
	public String listStockJob(){
		actionUtil.kuayu();
		jobAction.clear();
		List<Job> list=js.listStockJob();
		System.out.print(list.size());
		MapUtil.setStatus(jobAction, "1002");
		MapUtil.setOther(jobAction, list);
		MapUtil.setTotalNumber(jobAction, list.size());
		return "success";
	}
	//列举所有应聘信息
		public String listUNStockJob(){
			actionUtil.kuayu();
			jobAction.clear();
			List<Job> list=js.listUNStockJob();
			System.out.print(list.size());
			MapUtil.setStatus(jobAction, "1002");
			MapUtil.setOther(jobAction, list);
			MapUtil.setTotalNumber(jobAction, list.size());
			return "success";
		}
	/*//人才信息查看
	public String detailJob(){
		actionUtil.kuayu();
		//HttpServletResponse response=ServletActionContext.getResponse();
		//response.setHeader("Access-Control-Allow-Origin", "*");
		jobAction.clear();
		Long idd=Long.parseLong(jobs.getId().trim());
		Job job=js.detailJob(idd);
		MapUtil.setStatus(jobAction, "1002");
		MapUtil.setOther(jobAction, job);
		return "success";
	}*/
	
	//人才信息删除
	public String deleteJob(){
		actionUtil.kuayu();
		jobAction.clear();
		Job job=new Job();
		JobUtil.setJobId(job, jobs);
		js.deleteJob(job);
		MapUtil.setStatus(jobAction, "1002");//删除成功
		MapUtil.setOther(jobAction, "删除成功");
		return "success";
	}
	//人才信息入库
	public String stockJob(){
		actionUtil.kuayu();
		jobAction.clear();
		Long idd=Long.parseLong(jobs.getId().trim());
		Job job=js.stockJob(idd);
		MapUtil.setStatus(jobAction, "1002");
		MapUtil.setOther(jobAction, job);
		return "success";
	}

	@Override
	public JobString getModel() {
		// TODO 自动生成的方法存根
		return jobs;
	}
	public Map<String, Object> getJobAction() {
		return jobAction;
	}
   
}
