package util;

import java.util.Date;

import entity.User;
import entity.Users;

public class UserUtil {
	public static void setUsers(Users users,User user){
		if(user.getId()!=null){
		   Long idd=Long.parseLong(user.getId().trim());
		   users.setId(idd);
		}
		System.out.println(user.getId());
		if(!user.getUsername().equals("")){
		    users.setPassword(user.getPassword().trim());
		}
		users.setUsername(user.getUsername().trim());
		Byte sex=Byte.parseByte(user.getSex().trim());
		users.setSex(sex);
		Date birth = DateUtil.parseToDate(user.getBirthday().trim(), DateUtil.yyyyMMdd);
		users.setBirthday(birth);
		if(user.getCreatetime()!=null){//////////////
		Date create = DateUtil.parseToDate(user.getCreatetime().trim(), DateUtil.yyyyMMdd);
		users.setCreatetime(create);
		}////////////
		Byte admin=Byte.parseByte(user.getIsadmin().trim());
		users.setIsadmin(admin);
		users.setContent(user.getContent());
		System.out.println("User---->Users");
	}

}
