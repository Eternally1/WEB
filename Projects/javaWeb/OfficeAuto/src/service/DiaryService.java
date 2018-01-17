package service;

import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;

import util.DateUtil;
import dao.DiaryDao;
import dao.UserDao;
import entity.Diary;
import entity.DiarySend;
import entity.User;

public class DiaryService {
	DiaryDao dao = new DiaryDao();
	UserDao userdao = new UserDao();
	/**
	 * 添加日志
	 * @param dia
	 */
	public boolean addDiary(Diary dia){	
		Date now = new Date();
		Date date = DateUtil.parseToDate(now, DateUtil.yyyyMMdd);
		dia.setTime(date);
		if(!dao.existsDiary(dia.getTime(),dia.getUserID())){
			dao.addDiary(dia);
			return true;//成功添加
		}else{	
			return false;//已经存在
		}
	}
	/**
	 * 修改日志
	 * @param dia
	 */
	public void updateDiary(Diary dia){
		Date date = DateUtil.parseToDate(dia.getStrTime(), DateUtil.yyyyMMdd);
		dia.setTime(date);	
		dao.updateDiary(dia);
	}
	/**
	 * 员工
	 * 员工自己查询
	 * 根据员工id+日期：查询该员工的本月的日志
	 * 以列表形式返回
	 * @param userID
	 * @return
	 */
	public List<DiarySend> listDiarys_Month(String userID,String strTime){
		Date date = DateUtil.parseToDate(strTime, DateUtil.yyyyMMdd);
		List<Diary> list = dao.listDiarys_Month(userID,date);
		Iterator<Diary> it = list.iterator();
		List<DiarySend> resList = new ArrayList<DiarySend>();
		while(it.hasNext()){
			Diary diary = it.next();	
			User user = userdao.loadUser(userID);
			DiarySend send = new DiarySend();
			send.setId(diary.getId());
			send.setContent(diary.getContent());
			send.setTime(diary.getTime());
			send.setTitle(diary.getTitle());
			send.setUsername(user.getUsername());
			send.setUserID(userID);
			resList.add(send);
		}
		return resList;
	}
	/**
	 * 管理员
	 * 根据日期查询所有员工日志
	 * 以列表形式返回
	 * @param date
	 * @return
	 */
	public List<DiarySend> listDiarys_All(Diary dia){	
		Date date = DateUtil.parseToDate(dia.getStrTime(), DateUtil.yyyyMMdd);
		List<Diary> list = dao.listDiarys_All(date);
		Iterator<Diary> it = list.iterator();
		List<DiarySend> resList = new ArrayList<DiarySend>();
		while(it.hasNext()){
			Diary diary = it.next();	
			User user = userdao.loadUser(diary.getUserID());
			DiarySend send = new DiarySend();
			send.setId(diary.getId());
			send.setContent(diary.getContent());
			send.setTime(diary.getTime());
			send.setTitle(diary.getTitle());
			send.setUsername(user.getUsername());
			send.setUserID(diary.getUserID());
			resList.add(send);
		}
		
		
		return resList;
	}
	/**
	 * 加载日志内容
	 * @param id
	 * @return
	 */
	public DiarySend loadDiary(String userID,String strTime){
		Date date = DateUtil.parseToDate(strTime, DateUtil.yyyyMMdd);	
		boolean flag = dao.existsDiary(date, userID);
		if(flag){
			Diary diary = dao.loadDiary(userID,date);
			User user = userdao.loadUser(userID);
			DiarySend send = new DiarySend();
			send.setId(diary.getId());
			send.setContent(diary.getContent());
			send.setTime(diary.getTime());
			send.setTitle(diary.getTitle());
			send.setUsername(user.getUsername());
			send.setUserID(userID);
			return send;
		}else{
			return null;
		}		
	}
	
	
	

}
