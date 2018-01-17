package dao;

import org.hibernate.Query;
import org.hibernate.Session;

import util.SessionFactoryUtil;
import entity.Sentence;

public class SentenceDao {
	
	public Sentence getSentence(int id){
		Session session = SessionFactoryUtil.getSession();
		session.beginTransaction();
		Query query = session.createQuery("from Sentence where id=?");
		query.setParameter(0, id);
		Sentence sentence = (Sentence) query.list().get(0);
		session.getTransaction().commit();
		session.close();
		return sentence;
	}

}
