package action;

import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import service.AgendaService;
import util.DateUtil;
import util.MapUtil;

import com.opensymphony.xwork2.ActionSupport;
import com.opensymphony.xwork2.ModelDriven;

import entity.Agenda;

public class AgendaAction  extends ActionSupport implements ModelDriven<Agenda>{
    private Agenda agenda=new Agenda();
    private AgendaService agendaService=new AgendaService();
    private Map<String,Object> agendamap= new HashMap<String, Object>();
    private String time;
   
    public String getTime() {
		return time;
	}
	public void setTime(String time) {
		this.time = time;
	}
	public Map<String, Object> getAgendamap() {
		return agendamap;
	}
	public void setAgendamap(Map<String, Object> agendamap) {
		this.agendamap = agendamap;
	}
	//获取所有日程信息根据用户编号
    public String getAllAgenda(){
    	List<Agenda> agendas=agendaService.getAllAgenda(agenda.getUserID());
    	//添加状态码
    	MapUtil.setStatus(agendamap, "1001");
    	MapUtil.setOther(agendamap, agendas);
    	return "getsuccess";
    }
     //获取所有日程信息根据用户编号与时间
  		public String getAgendaByIdAndTime(){
  			List<Agenda> list=agendaService.getAgendaByIdAndTime(agenda.getUserID(), time);
  		//添加状态码
  	    	MapUtil.setStatus(agendamap, "1001");
  	    	MapUtil.setOther(agendamap, list);
			return "getsuccess";
  		}
  	  //添加日程
	public String addAgenda() {
		// 判断开始时间是否早于结束时间
		boolean falg = DateUtil.compareTime(agenda.getBegintime(),
				agenda.getFinishtime());
		if (falg == false) {
			MapUtil.setStatus(agendamap, "1002");
			// 添加信息
			MapUtil.setOther(agendamap, "开始时间早于结束时间");
			return "addfailed";
		} else {
			agendaService.addAgenda(agenda);
			// 添加状态码
			MapUtil.setStatus(agendamap, "1001");
			// 添加信息
			MapUtil.setOther(agendamap, "添加成功");
			return "addsuccess";
		}
	}
    //更新日程
    public String updateAgenda(){

    	agendaService.updateAgenda(agenda);
    	MapUtil.setStatus(agendamap, "1001");
    	MapUtil.setOther(agendamap, "更新成功");
		return "updatesuccess";
    }
    //删除日程
    public String deleteAgenda(){

    	agendaService.deleteAgenda(agenda);
    	MapUtil.setStatus(agendamap, "1001");
    	MapUtil.setOther(agendamap, "已删除");
		return "deletesuccess";
    }
    //完成日程
    public String finishAgenda(){
    	agendaService.finishAgenda(agenda);
    	MapUtil.setStatus(agendamap, "1001");
    	MapUtil.setOther(agendamap, "已完成");
		return "finishsuccess";
    }
    /**
     * 获取最近日程，用于日程提醒
     * 输入：strDate+userID
     * 返回：Date time
     * @return
     */
    public String getNewestAgenda(){
    	Agenda newestAgenda = agendaService.getNewestAgenda(agenda);
    	if(newestAgenda == null){
    		//当天无日程
    		MapUtil.setStatus(agendamap, "1001");
    		MapUtil.setOther(agendamap, null);
    		return "failed";
    	}else{
    		//下一条日程
    		MapUtil.setStatus(agendamap, "1001");
    		MapUtil.setOther(agendamap, newestAgenda);
    		return "success";
    	}
    }
    //首页修改日程信息
    public String changeAgendaState(){
    	agendaService.changeAgendaState(agenda);
    	MapUtil.setStatus(agendamap, "1001");
    	MapUtil.setOther(agendamap, "修改状态成功");
    	return "changesuccess";
    }
    
	@Override
	public Agenda getModel() {
		// TODO 自动生成的方法存根
		return agenda;
	}

}
