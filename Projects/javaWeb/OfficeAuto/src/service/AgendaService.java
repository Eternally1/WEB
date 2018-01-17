package service;

import java.util.Date;
import java.util.List;

import util.DateUtil;
import dao.AgendaDao;
import dao.UserDao;
import entity.Agenda;
import entity.User;

public class AgendaService {
	private AgendaDao agendaDao=new AgendaDao();
	private UserDao userDao=new UserDao();
	//获取所有日程信息根据用户编号
	public List<Agenda> getAllAgenda(String userID){
		List<Agenda>  list=agendaDao.getAllAgenda(userID);
		return list;
	}
	//添加用户日程
	public void addAgenda(Agenda agenda){
		agenda.setState(0);//设置状态为未完成
		//设置起始日程
		String nowdate=getNowTime();
		String starttime=nowdate+" "+agenda.getBegintime();
		String endtime=nowdate+" "+agenda.getFinishtime();
		Date startTime=DateUtil.parseToDate(starttime,DateUtil.yyyyMMddHHmm );
		Date endTime=DateUtil.parseToDate(endtime, DateUtil.yyyyMMddHHmm);
		agenda.setStarttime(startTime);
		agenda.setEndtime(endTime);
		//添加日程
		agendaDao.addAgenda(agenda);
	}
	//获取所有日程信息根据用户编号与时间
		public List<Agenda> getAgendaByIdAndTime(String userID,String time){
			List<Agenda> list=agendaDao.getAgendaByIdAndTime(userID, time);
			return list;
		}
	//更新日程信息
	public void updateAgenda(Agenda agenda){
		Date startTime=DateUtil.parseToDate(agenda.getBegintime(),DateUtil.yyyyMMddHHmm );
		Date endTime=DateUtil.parseToDate(agenda.getFinishtime(), DateUtil.yyyyMMddHHmm);
		agenda.setStarttime(startTime);
		agenda.setEndtime(endTime);
		agenda.setState(0);
		agendaDao.updateAgenda(agenda);
	}
	//删除日程信息，更新state状态为2
	public void deleteAgenda(Agenda agenda){
		//1、前台传给我id和content
	   Agenda agda=agendaDao.getAgenda(agenda.getId());
	   agda.setState(2);
	   agendaDao.updateAgenda(agda);
	}
	//完成日程信息，更新state状态为1
	public void finishAgenda(Agenda agenda) {
		// 1、前台传给我id
		Agenda agda = agendaDao.getAgenda(agenda.getId());
		agda.setState(1);
		agendaDao.updateAgenda(agda);
	}
	//获取当前系统时间
	private String getNowTime(){
		Date date=new Date();
		String nowdate=DateUtil.parseToString(date, DateUtil.yyyyMMdd);
		return nowdate;
	}
	
	public Agenda getNewestAgenda(Agenda agenda){
		Date date = new Date();
		String nowTime = DateUtil.parseToString(date, DateUtil.yyyyMMdd);
		Date dayEnd = DateUtil.parseToDate(nowTime+" 23:59:59", DateUtil.yyyyMMddHHmmss);
		return agendaDao.getNewestAgenda(agenda,dayEnd);
	}
	  //首页修改日程信息，更新state状态为0
	public void changeAgendaState(Agenda agenda) {
		// 1、前台传给我id
		Agenda agda = agendaDao.getAgenda(agenda.getId());
		agda.setState(0);
		agendaDao.updateAgenda(agda);
	}

}
