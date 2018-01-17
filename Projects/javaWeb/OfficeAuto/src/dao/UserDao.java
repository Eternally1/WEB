package dao;

import java.util.Iterator;
import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;

import util.SessionFactoryUtil;
import entity.User;

public class UserDao {
	//获取用户信息
	public User getUser(String userID){
		Session session=SessionFactoryUtil.getSession();
		session.beginTransaction();
		User user=(User) session.get(User.class, userID);
		session.getTransaction().commit();
	    session.close();
		return user;
	}
	//根据用户名获取信息
	public List<User> getUserByUserName(String userName){
		Session session=SessionFactoryUtil.getSession();
		session.beginTransaction();
		Query query=session.createQuery("from User where username=?");
		query.setParameter(0, userName);
		List<User> list=query.list();
		session.getTransaction().commit();
		session.close();
		return list;
	}
	//根据用户名和用户ID获取
	public User getUserByIdAndName(String id,String name){
		Session session=SessionFactoryUtil.getSession();
		session.beginTransaction();
		Query query=session.createQuery("from User where username=? and userID=?");
		query.setParameter(0, name);
		query.setParameter(1, id);
		List<User> list=query.list();
		User user=list.get(0);
		session.getTransaction().commit();
		session.close();
		return user;
	}
     public User loadUser(String userID){
		Session session = SessionFactoryUtil.getSession();
		session.beginTransaction();
		User user = (User) session.get(User.class, userID);
		session.getTransaction().commit();
		session.close();
		return user;
	}
	//登录验证
	public boolean existUser(User user) {//每个用户的员工号不一样，可通过员工号判断用户是否存在
		Session session=SessionFactoryUtil.getSession();
		session.beginTransaction();
		Query query=session.createQuery("select userID from User where userID=? and password=? ");
		query.setParameter(0,user.getUserID().trim());
		query.setParameter(1, user.getPassword().trim());
		List<String> list=query.list();
		session.getTransaction().commit();
		session.close();
		if(!list.isEmpty()){//存在
			//获取用户姓名：学生显示姓名，管理员显示编号
			return true;
		}
		return false;//不存在
	}
	//注册用户
	public void saveUser(User user){
		Session session=SessionFactoryUtil.getSession();
		session.beginTransaction();
		session.save(user);
		session.getTransaction().commit();
		session.close();
	}
	//获取数据库表的记录数
	public int listSize(){
		Session session = SessionFactoryUtil.getSession();
		session.beginTransaction();
		Query query = session.createQuery("from User");
		int size = query.list().size();
		session.getTransaction().commit();
		session.close();
		return size;
	}

}


