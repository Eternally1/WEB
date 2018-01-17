package util;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DateUtil {
	public static final String yyyyMMddHHmmss = "yyyy-MM-dd HH:mm:ss";// 自动生成格式
	public static final String yyyyMMddHHmm = "yyyy-MM-dd HH:mm";
	public static final String yyyyMMdd = "yyyy-MM-dd";// 日志日期
	public static final String yyyMMdd = "yyyyMMdd";// 日志日期

	/**
	 * 字符串转日期时间格式
	 * 
	 * @param s
	 * @param style
	 * @return
	 */
	public static Date parseToDate(String s, String style) {
		SimpleDateFormat format = new SimpleDateFormat();
		format.applyPattern(style);

		Date date = null;
		if (s == null || s.length() < 8) {
			return null;
		}
		try {
			date = format.parse(s);
		} catch (ParseException e) {
			e.printStackTrace();
		}
		return date;
	}

	/**
	 * 格式化日期字符串
	 */
	public static String parseToString(String s, String style) {
		SimpleDateFormat format = new SimpleDateFormat();
		format.applyPattern(style);

		Date date = null;
		String str = null;
		if (s == null || s.length() < 8) {
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
	public static String parseToString(Date date, String style) {
		SimpleDateFormat format = new SimpleDateFormat();
		format.applyPattern(style);
		String str = null;
		if (date == null)
			return null;
		str = format.format(date);
		return str;
	}

	/**
	 * 日期格式调整
	 */
	public static Date parseToDate(Date date, String style) {
		SimpleDateFormat format = new SimpleDateFormat();
		format.applyPattern(style);
		String strDate = format.format(date);
		Date newDate = null;
		if (date == null) {
			return null;
		}
		try {
			newDate = format.parse(strDate);
		} catch (ParseException e) {
			e.printStackTrace();
		}
		return newDate;
	}

	// 判断日期是否相等
	public static boolean compareDate(String date, Date date1) {
		String date2 = parseToString(date1, DateUtil.yyyyMMddHHmm);
		System.out.println(date2);
		if (date.equals(date2)) {
			return true;
		}
		return false;
	}

	// 判断开始时间是否早于结束时间
	public static boolean compareTime(String begintime, String endtime) {
		String h1 = begintime.split(":")[0];
		String m1 = begintime.split(":")[1];
		String h2 = endtime.split(":")[0];
		String m2 = endtime.split(":")[1];
		int hour1 = Integer.parseInt(h1);
		int hour2 = Integer.parseInt(h2);
		int minute1 = Integer.parseInt(m1);
		int minute2 = Integer.parseInt(m2);
		if (hour1 > hour2) {
			return false;
		} else if (hour1 == hour2) {
			if (minute1 >= minute2) {
				return false;
			} else {
				return true;
			}
		} else {
			return true;
		}
	}

}
