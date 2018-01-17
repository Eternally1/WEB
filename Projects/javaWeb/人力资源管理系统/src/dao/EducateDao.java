package dao;

import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;

import util.HibernateSessionFactory;
import entity.Educate;

/**
 * 培训信息dao类
 * @author 董元杰
 *
 */

public class EducateDao {
	
	/**
	 * 培训计划录入
	 * @param educate
	 */
	public void addEducate(Educate educate){
		educate.setCreatetime(new java.util.Date());
		Session session = HibernateSessionFactory.getSession();
		session.beginTransaction();
		session.save(educate);
		session.getTransaction().commit();
		HibernateSessionFactory.closeSession();
	}
	
	/**
	 * 培训计划是否存在
	 */
	public boolean ExistsEducate(Educate e){
		Session session = HibernateSessionFactory.getSession();
		//根据姓名看是否存在不合理，看数据库中已经存在多个一样的名字
		Query query = session.createQuery("select id from Educate where name=:name");
		query.setParameter("name", e.getName());
		
		if(query.list().isEmpty()){
			return false;//不存在，可以插入
		}		
		return true;
	}

	/**
	 * 培训计划列表查看
	 */
	public List<Educate> listEducate(){
		Session session = HibernateSessionFactory.getSession();
		Query query = session.createSQLQuery("select * from Educate order by createtime").addEntity(Educate.class);
		
		List<Educate> list = query.list();	
		HibernateSessionFactory.closeSession();
		
		return list;
	}
	
	/**
	 * 培训计划详情
	 */
	public Educate loadEducate(Long id){
		Session session = HibernateSessionFactory.getSession();
		Educate educate = (Educate) session.get(Educate.class, id);
		HibernateSessionFactory.closeSession();
		
		return educate;
	}
	/**
	 * 培训计划删除
	 */
	public void deleteEducate(Educate educate){
		Session session = HibernateSessionFactory.getSession();
		session.beginTransaction();
		session.delete(educate);
		session.getTransaction().commit();
		HibernateSessionFactory.closeSession();
	}
	
}
