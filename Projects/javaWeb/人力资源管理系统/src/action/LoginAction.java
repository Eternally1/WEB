package action;

import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import service.UsersService;
import util.DateUtil;
import util.MapUtil;





import util.UserUtil;
import util.actionUtil;

import com.opensymphony.xwork2.ActionSupport;
import com.opensymphony.xwork2.ModelDriven;

import entity.User;
import entity.Users;

public class LoginAction extends ActionSupport implements ModelDriven<User>   {
	private UsersService userService=new UsersService();
	private User user=new User();
    private Map<String,Object> loginSuccess= new HashMap<String, Object>();
	
	public String login() throws Exception {
	  actionUtil.kuayu();
//	  System.out.print("你哈");
	  String flag="";
       loginSuccess.clear();
//		System.out.print(user.getUsername());
		if(userService.check(user)){
			loginSuccess.put("user",user);
			loginSuccess.put("status", "1002");
			flag="success";
		}else{
		   flag="failed";
		   MapUtil.setStatus(loginSuccess, "1001");
		   MapUtil.setOther(loginSuccess, "登录失败");
		}
		return flag;
	}
	//添加用户测试不了birthday设置为了日期格式无法直接自己给参数
	//一直没注入到user中去
	public String addUsers(){
		String flag="";
		actionUtil.kuayu();
		Users users=new Users();
		UserUtil.setUsers(users, user);
		loginSuccess.clear();
		if(userService.addUser(users)){
		   MapUtil.setStatus(loginSuccess, "1002");
		   MapUtil.setOther(loginSuccess, "添加成功");
		   flag="success";
		}else{
			System.out.print(users.getPassword()+users.getUsername());
	      MapUtil.setStatus(loginSuccess, "1001");
	      if(user.getUsername().equals("")&&user.getPassword().equals("")){
	    	  MapUtil.setOther(loginSuccess, "用户名或密码为空");
	      }else{
	    	  MapUtil.setOther(loginSuccess, "用户已存在");
	      }
		  flag="false";
		}
		  return flag;
	}
	//显示全部用户，没设置失败的情况
	public String  listUser(){
		actionUtil.kuayu();
		List<User> list=userService.listUser();
		loginSuccess.clear();
		MapUtil.setStatus(loginSuccess, "1002");
		MapUtil.setOther(loginSuccess, list);
		MapUtil.setTotalNumber(loginSuccess, list.size());
		return  "success";
	}
	//删除用户信息
	public String deleteUser(){
		actionUtil.kuayu();
//		System.out.println(user.getId());
		loginSuccess.clear();
		Long idd=Long.parseLong(user.getId().trim());
//		System.out.println(idd);
		userService.deleteUser(idd);
		MapUtil.setStatus(loginSuccess, "1002");
		MapUtil.setOther(loginSuccess, "删除用户成功");////////////
		return SUCCESS;
		
	}
	//更新用户信息
	public  String updateUser(){
		actionUtil.kuayu();
		loginSuccess.clear();
		Users users=new Users();
		UserUtil.setUsers(users, user);
		userService.updateUser(users);
		MapUtil.setStatus(loginSuccess, "1002");
		MapUtil.setOther(loginSuccess, "更新用户成功");//////////
		return SUCCESS;
		
	}
	
	public Map<String, Object> getLoginSuccess() {
		return loginSuccess;
	}
	@Override
	public User getModel() {
		// TODO 自动生成的方法存根
		return user;
	}
}
