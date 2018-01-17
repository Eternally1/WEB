package service;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import util.DateUtil;
import dao.UsersDao;
import entity.User;
import entity.Users;


public class UsersService {
	UsersDao dao = new UsersDao();
	//验证登录
	public boolean check(User user){
		if(dao.exists(user)){
			return true;
		}
		return false;	
	}
	//添加用户
	public boolean addUser(Users users){
		User user=new User();
		user.setPassword(users.getPassword());
		user.setUsername(users.getUsername());
		if(!dao.exists(user)&&!user.getUsername().equals("")&&!user.getPassword().equals("")){
		  dao.addUsers(users);
		  System.out.println("添加人员成功");
		  return true;
		}
		return false;
	}
	//显示所有用户
	public List<User> listUser(){
		List<Users> list=dao.listUser();
		List<User> listRes = new ArrayList<User>();
		Iterator it = list.iterator();
		while(it.hasNext()){
			Users u = (Users) it.next();
			User user = new User();
			user.setId(u.getId().toString().trim());
			user.setUsername(u.getUsername());
			user.setPassword(u.getPassword());
			user.setSex(u.getSex().toString());
			user.setIsadmin(u.getIsadmin().toString());
			String birth = DateUtil.parseToString(u.getBirthday(), DateUtil.yyyyMMdd);
			user.setBirthday(birth);
			user.setContent(u.getContent());
			listRes.add(user);		
		}
		System.out.println("列举成功");
		return listRes;

	}
	//删除用户信息
	public void deleteUser(Long id){
		Users user=new Users();
		user.setId(id);
		dao.deleteUsers(user);
		System.out.println("删除成功");
	}
	//更新用户信息
	public void updateUser(Users users){
		dao.update(users);
		System.out.print("更新用户"+users.getUsername()+"成功");
	}
}
