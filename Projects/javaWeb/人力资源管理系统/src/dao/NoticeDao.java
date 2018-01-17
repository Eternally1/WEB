package dao;

import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;

import util.HibernateSessionFactory;
import entity.Notice;

public class NoticeDao {
	
	public void AddNotice(Notice notice){
		notice.setCreatetime(new java.util.Date());
		Session session = HibernateSessionFactory.getSession();
		session.beginTransaction();
		session.save(notice);
		session.getTransaction().commit();
		HibernateSessionFactory.closeSession();
	}
	
	public List<Notice> listNotice(){
		Session session = HibernateSessionFactory.getSession();	
		Query query = session.createSQLQuery("select * from Notice order by createtime").addEntity(Notice.class);
		List<Notice> list = query.list();
		HibernateSessionFactory.closeSession();	
		return list;
	}
	
	public Notice loadNotice(Long id){
		Session session = HibernateSessionFactory.getSession();
		Notice notice = (Notice) session.load(Notice.class, id);
		HibernateSessionFactory.closeSession();	
		return notice;
	}
	
	

}
