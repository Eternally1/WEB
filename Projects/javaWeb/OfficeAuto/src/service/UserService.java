package service;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import util.DateUtil;
import dao.UserDao;
import entity.User;

public class UserService {
	private static int count=1;
	private UserDao userDao=new UserDao();
	//登录验证
	public boolean existUser(User user){
		boolean flag=userDao.existUser(user);
		return flag;
	}
	//获取用户信息
	public User getUserByID(String userID){
		User user=userDao.getUser(userID);
		return user;
	}
	//注册用户
	public void saveUser(User user){
		//获取当前系统时间
	    Date date=new Date();
	    String date1=DateUtil.parseToString(date, DateUtil.yyyMMdd);
	    int listSize = userDao.listSize();
	    user.setUserID(date1+listSize);
	    userDao.saveUser(user);
	}
	//根据搜索栏传回的用户名或用户ID进行整合获取用户信息
	public List<User> getUsers(String serachStr){
		//User user1=userDao.getUserByIdAndName(serachStr, serachStr);
		User user=userDao.getUser(serachStr);
		List<User> list=userDao.getUserByUserName(serachStr);
		if(user!=null){
			list.add(user);
		}
		//if(user1!=null){
		for(User u:list){
			if(u.getUserID().equals(u.getUsername())){
				System.out.println(u.getUsername());
				list.remove(u);
			}
		}
 	//}
		return list;
  }
}
