package service;

import java.util.Random;

import dao.SentenceDao;

public class SentenceService {
	private SentenceDao dao = new SentenceDao();
	public String getSentence(){
		Random ran = new Random();
		int id = ran.nextInt(20)+1;
		return dao.getSentence(id).getSent();
	}
}
