package dao;

import java.util.List;
import org.hibernate.Query;
import org.hibernate.Session;
import util.HibernateSessionFactory;
import entity.Job;

/**
 * 应聘人员dao类
 * @author 董元杰
 *
 */

public class JobDao {
	
	/**
	 * 应聘信息录入
	 */
	public void addJob(Job job){
		job.setCreatetime(new java.util.Date());//设置当前时间
		job.setIsstock(new Byte("0"));//设置入库信息为0，表示暂时不入库
		Session session = HibernateSessionFactory.getSession();
		session.beginTransaction();
		session.save(job);
		session.getTransaction().commit();
		HibernateSessionFactory.closeSession();
	}
	/**
	 * 查看是否存在
	 */
	public boolean ExistsJob(Job job){
		Session session = HibernateSessionFactory.getSession();
		
		Query query = session.createQuery("select id from Job where name=:name");
		query.setParameter("name", job.getName());
		
		if(query.list().isEmpty()){
			return false;
		}	
		return true;
	}
	/**
	 * 应聘人员列表查看
	 */
	public List<Job> listJob(){
		Session session = HibernateSessionFactory.getSession();
		
		Query query = session.createSQLQuery("select * from job order by createtime").addEntity(Job.class);
		
		List<Job> list = query.list();
		return list;
	}
	
	/**
	 * 应聘人员详细信息
	 */
	public Job loadJob(Long id){
		Session session = HibernateSessionFactory.getSession();
		Job job = (Job) session.get(Job.class, id);
		HibernateSessionFactory.closeSession();
		return job;
	}
	/**
 * 加入人才库
   */
	public void Stock(Job job){
		Session session = HibernateSessionFactory.getSession();
		session.beginTransaction();
		job.setIsstock(new Byte("1"));    //表示人才入库
		session.update(job);
		session.getTransaction().commit();
    	HibernateSessionFactory.closeSession();
	}
	
	/**
	 * 删除应聘人员信息
	 */
	public void deleteJob(Job job){
		Session session = HibernateSessionFactory.getSession();
		session.beginTransaction();
		session.delete(job);
		session.getTransaction().commit();
		HibernateSessionFactory.getSession();
	}

}
