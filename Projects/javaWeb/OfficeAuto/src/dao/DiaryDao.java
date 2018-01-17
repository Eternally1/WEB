package dao;

import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;

import util.SessionFactoryUtil;
import entity.Diary;
import entity.User;

public class DiaryDao {
	/**
	 * 添加日志
	 * @param dia
	 */
	public void addDiary(Diary dia){
		Session session = SessionFactoryUtil.getSession();//获取session实例
		session.beginTransaction();
		session.save(dia);
		session.getTransaction().commit();
		session.close();
	}
	/**
	 * 查询当天日志是否存在:false为不存在，true为存在
	 * @param dia
	 * @return
	 */
	public boolean existsDiary(Date time,String userID){
		Session session = SessionFactoryUtil.getSession();
		session.beginTransaction();
		Query query = session.createQuery("from Diary where time = ? and userID = ?");
		query.setParameter(0, time);
		query.setParameter(1, userID);
		List list = query.list();
		//将数据库查询结果保存到对象后再提交事务，关闭session
		session.getTransaction().commit();
		session.close();
		if(list.isEmpty()){
			//不存在
			return false;
		}
		return true;
	}
	/**
	 * 修改日志
	 * @param dia
	 */
	public void updateDiary(Diary dia){
		Session session = SessionFactoryUtil.getSession();
		session.beginTransaction();
		session.update(dia);
		session.getTransaction().commit();
		session.close();
	}
	/**
	 * 根据日志id加载日志信息
	 * 显示日志内容在浏览器右侧
	 * @param id
	 * @return
	 */
	public Diary loadDiary(String userID,Date time){
		Diary dia = new Diary();
		Session session = SessionFactoryUtil.getSession();
		session.beginTransaction();
		Query query = session.createQuery("from Diary where userID=? and time=?");
		query.setParameter(0, userID);
		query.setParameter(1, time);
		dia = (Diary) query.list().get(0);
		session.getTransaction().commit();
		session.close();
		return dia;
	}
	/**
	 * 员工自己查询
	 * 根据员工id+日期：查询该员工的本月的日志
	 * 以列表形式返回
	 * @param userID
	 * @param date
	 * @return
	 */
	public List<Diary> listDiarys_Month(String userID,Date date){
		List<Diary> list = new ArrayList<Diary>();
		Session session = SessionFactoryUtil.getSession();
		session.beginTransaction();
		Query query = session.createQuery("from Diary where userID = ? and DATE_FORMAT(time,'%Y%m')=DATE_FORMAT(?,'%Y%m')");
		query.setParameter(0, userID);
		query.setParameter(1, date);
		list = query.list();
		session.getTransaction().commit();
		session.close();
		return list;		
	}
	/**
	 * 管理员
	 * 根据日期查询所有员工日志
	 * 以列表形式返回
	 * @param date
	 * @return
	 */
	public List<Diary> listDiarys_All(Date date){
		List<Diary> list = new ArrayList<Diary>();
		Session session = SessionFactoryUtil.getSession();
		session.beginTransaction();
		Query query = session.createQuery("from Diary where time=?");
		query.setParameter(0, date);
		list = query.list();
		session.getTransaction().commit();
		session.close();
		return list;
	}

}
