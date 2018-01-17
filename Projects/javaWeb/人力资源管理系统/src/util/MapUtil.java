package util;

import java.util.Map;

import action.LoginAction;

public class MapUtil {
	//添加状态码
	public static void setStatus(Map<String,Object> map,String status){
		map.put("status", status);
	}
	//添加获取的对象数据
	public static void setOther(Map<String,Object> map,Object obj){
		map.put("data", obj);
	}
	//添加数据总条数
	public static void setTotalNumber(Map<String,Object> map,int count){
		map.put("totalNumber", count);
	}

}
