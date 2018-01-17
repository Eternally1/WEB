package util;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class HibernateSessionFactory {
	static Configuration conf = null;
	static SessionFactory sf = null;
	static Session session = null;
	public static Session getSession(){
		conf=new Configuration();  
        conf.configure("hibernate.cfg.xml");  
        //获取session工厂
        sf=conf.buildSessionFactory();  
        //获取session实例  
        session=sf.openSession();  
        return session;
	}
	
	public static void closeSession(){
		session.close();
		sf.close();
	}

}
