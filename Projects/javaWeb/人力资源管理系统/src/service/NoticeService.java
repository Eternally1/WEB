package service;

import java.util.List;

import dao.NoticeDao;
import entity.Notice;

public class NoticeService {
	private  NoticeDao nod=new NoticeDao();
	//列举所有公告
	public List<Notice> listNotice(){
		List<Notice> list=nod.listNotice();
		return list;
	}

}
