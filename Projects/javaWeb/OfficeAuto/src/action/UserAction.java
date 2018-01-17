package action;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import service.UserService;
import util.MapUtil;

import com.opensymphony.xwork2.ActionSupport;
import com.opensymphony.xwork2.ModelDriven;

import entity.User;
import entity.UserSend;

public class UserAction extends ActionSupport implements ModelDriven<User>{
	private String serachStr;
	private String tel_reg = "^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1}))+\\d{8})$";
	private String email_reg =" ^\\w+((-\\w+)|(\\.\\w+))*\\@[A-Za-z0-9]+((\\.|-)[A-Za-z0-9]+)*\\.[A-Za-z0-9]+$";
	public String getSerachStr() {
		return serachStr;
	}
	public void setSerachStr(String serachStr) {
		this.serachStr = serachStr;
	}
	private User user=new User();
	private UserService userService=new UserService();
	private Map<String,Object> usermap= new HashMap<String, Object>();
   public Map<String, Object> getUsermap() {
		return usermap;
	}
	public void setUsermap(Map<String, Object> usermap) {
		this.usermap = usermap;
	}
	//登录验证
	public String loginCheck(){
		boolean flag=userService.existUser(user);
		if(flag==true){
			User user1=userService.getUserByID(user.getUserID());
			UserSend usersend=new UserSend(user1.getUsername(),user1.getRole(),user1.getUserID(),user1.getGender());
			MapUtil.setStatus(usermap, "1001");
			MapUtil.setOther(usermap, "登录成功");
			MapUtil.setUser(usermap, usersend);
			return "getsuccess";
		}else {
			MapUtil.setStatus(usermap, "1002");
			User user2=userService.getUserByID(user.getUserID());
			if(user2!=null){
				MapUtil.setOther(usermap, "用户密码错误");
			}else{
			    MapUtil.setOther(usermap, "用户不存在");
			}
			return "getfailed";
		} 
	}
	//注册
		public String saveUser(){
			//判断手机号和邮箱是否符合格式
			

			  userService.saveUser(user);
			  MapUtil.setStatus(usermap, "1001");
			  MapUtil.setOther(usermap, "注册成功");
			  MapUtil.setUser(usermap, user);
			return "savesuccess";
			
		}
	//搜索用户信息
	public String searchUser(){
		List<User> list=userService.getUsers(serachStr);
		MapUtil.setStatus(usermap, "1001");
		MapUtil.setOther(usermap, "获取成功");
		MapUtil.setUser(usermap, list);
		return "searchsuccess";
	}
	@Override
	public User getModel() {
		// TODO 自动生成的方法存根
		return user;
	}

}
