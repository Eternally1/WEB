package util;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DateUtil {
	
	public static final String yyMMdd="yy-MM-dd";	//短日期格式
	public static final String yyyyMMdd="yyyy-MM-dd";//长日期格式
	public static final String HHmmss="HH:mm:ss";	//时间格式
	public static final String yyyyMMddHHmmss="yyyy-MM-dd HH:mm:ss";//长日期时间格式
	public static final String yyMMddHHmmss="yy-MM-dd HH:mm:ss";//短日期时间格式
	/**
	 * 字符串转日期时间格式
	 * @param s
	 * @param style
	 * @return
	 */
	public static Date parseToDate(String s,String style){
		SimpleDateFormat format = new SimpleDateFormat();
		format.applyPattern(style);//�ύת����ʽ
		
		Date date = null;
		if(s==null || s.length()<8){   //�ַ�Ϊ�ջ��߳���С��8
			return null;      //�޷�ת��������null
		}
		try {
			date = format.parse(s);    //ת��
		} catch (ParseException e) {
			e.printStackTrace();
		}	
		return date;
	}
	
	/**
	 * 格式化日期字符串
	 */
	public static String parseToString(String s,String style){
		SimpleDateFormat format = new SimpleDateFormat();
		format.applyPattern(style);
		
		Date date = null;
		String str = null;
		if(s==null || s.length()<8){
			return null;
		}
		try {
			date = format.parse(s);
			str = format.format(date);
		} catch (ParseException e) {
			e.printStackTrace();
		}
		return str;
	}
	/**
	 * 日期时间转字符串
	 */
	public static String parseToString(Date date,String style){
		SimpleDateFormat format = new SimpleDateFormat();
		format.applyPattern(style);
		String str = null;
		if(date==null)
			return null;
		str = format.format(date);
		return str;
	}

}
