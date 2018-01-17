package util;

import javax.servlet.http.HttpServletResponse;

import org.apache.struts2.ServletActionContext;

public class actionUtil  {
	//跨域问题
	public static void kuayu(){
		HttpServletResponse response=ServletActionContext.getResponse();
		response.setHeader("Access-Control-Allow-Origin", "*");
	}

}
