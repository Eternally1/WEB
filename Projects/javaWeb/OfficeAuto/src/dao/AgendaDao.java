package dao;

import java.util.Date;
import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;

import util.DateUtil;
import util.SessionFactoryUtil;
import entity.Agenda;

public class AgendaDao {
	//获取所有日程信息根据用户编号
	public List<Agenda> getAllAgenda(String userID){
		Session session=SessionFactoryUtil.getSession();
		session.beginTransaction();
		Query query=session.createQuery("from Agenda where userID=?");
		query.setParameter(0,userID);
		List<Agenda> list=query.list();
		session.getTransaction().commit();
		session.close();
		return list;
	}
	//获取所有日程信息根据用户编号与时间
	public List<Agenda> getAgendaByIdAndTime(String userID,String time){
		String time1=time+" "+"00:00:00";
		String time2=time+" "+"23:59:59";
		Session session=SessionFactoryUtil.getSession();
		session.beginTransaction();
		Query query=session.createQuery("from Agenda where starttime between ? and ? and userID=?");
		query.setParameter(0, DateUtil.parseToDate(time1, DateUtil.yyyyMMddHHmmss));
		query.setParameter(1, DateUtil.parseToDate(time2, DateUtil.yyyyMMddHHmmss));
		query.setParameter(2, userID);
		List<Agenda> list=query.list();
		session.getTransaction().commit();
		session.close();
		return list;
	}
	//获取用户日程根据日程id
	public Agenda getAgenda(int id){
		Session session=SessionFactoryUtil.getSession();
		Agenda agenda=(Agenda) session.get(Agenda.class, id);
		session.close();
		return agenda;
	}
	//添加用户日程
	public void addAgenda(Agenda agenda){
		Session session=SessionFactoryUtil.getSession();
		session.beginTransaction();
		session.save(agenda);
		session.getTransaction().commit();
		session.close();
	}
	//根据用户名和日程发布时间修改日程信息
	public void updateAgenda(Agenda agenda){
		//假设前台会把所有信息发过来，若没发，则根据用户名和日程发布时间获取该日程信息在进行更新
		Session session=SessionFactoryUtil.getSession();   
    	session.beginTransaction();
    	session.update(agenda);
    	session.getTransaction().commit();
    	session.close();
	}
	/**
	 * 获取距当前系统时间最近的日程
	 * @return
	 */
	public Agenda getNewestAgenda(Agenda agenda,Date dayEnd){
		Session session = SessionFactoryUtil.getSession();
		session.beginTransaction();
		Query query = session.createQuery("from Agenda where state = 0 and userID = ? and starttime BETWEEN NOW() and ? ORDER BY starttime ASC");
		query.setParameter(0, agenda.getUserID());
		query.setParameter(1, dayEnd);
		List list = query.list();
		session.getTransaction().commit();
		session.close();
		if(list.isEmpty()){
			return null;
		}
		return (Agenda)list.get(0);
	}
}
