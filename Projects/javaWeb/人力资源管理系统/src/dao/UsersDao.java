package dao;

import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;

import util.HibernateSessionFactory;
import entity.User;
import entity.Users;

public class UsersDao{
	/**
	 * 人员信息录入
	 * @param users
	 */
	public void addUsers(Users users){
		users.setCreatetime(new java.util.Date());//创建时间	
		Session session = HibernateSessionFactory.getSession();//session实例     
        session.beginTransaction();  //开启事务
        session.save(users);//保存用户
        session.getTransaction().commit(); //提交事务 
        HibernateSessionFactory.closeSession();
	}
	/**
	 * 查找人员是否存在
	 */
	public boolean exists(User users){
		Session session = HibernateSessionFactory.getSession();
		
        Query query = session.createQuery("select id from Users where username=:username and password=:password");
        query.setParameter("username", users.getUsername());
        query.setParameter("password", users.getPassword());
        if(query.list().isEmpty()){
        	return false;//不存在
        }
		return true;//存在
	}
	/**
	 * 根据id加载人员信息
	 */
	public Users loadUsers(Long id){
		Session session = HibernateSessionFactory.getSession();        		
		Users u = (Users)session.get(Users.class, id);//加载指定用户名的Users对象
		return u;
	}
	/**
	 * 人员信息查看 
	 */
	public List<Users> listUser(){
		Session session = HibernateSessionFactory.getSession();	
		Query query = session.createSQLQuery("select * from Users order by createtime").addEntity(Users.class);
		List<Users> list = query.list();
		HibernateSessionFactory.closeSession();
		return list;		
	}
	
	/**
	 * 人员信息修改
	 */
	public void update(Users user){	
		Users u = this.loadUsers(user.getId());
			u.setBirthday(user.getBirthday());
			u.setSex(user.getSex());
			u.setContent(user.getContent());
			u.setIsadmin(user.getIsadmin());
			u.setPassword(user.getPassword());
		Session session = HibernateSessionFactory.getSession();
		session.beginTransaction();
		session.update(u);
		session.getTransaction().commit();
		HibernateSessionFactory.closeSession();		
	}
	
	/**
	 * 人员信息删除
	 */
	public void deleteUsers(Users user){
		Session session = HibernateSessionFactory.getSession();
		session.beginTransaction();
		session.delete(user);
		session.getTransaction().commit();
		HibernateSessionFactory.closeSession();	
	}

}
