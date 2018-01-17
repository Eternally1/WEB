package util;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class SessionFactoryUtil {
	static Configuration conf = null;
	static SessionFactory sf = null;
	
	static{
		conf=new Configuration();  
        conf.configure("hibernate.cfg.xml");  
        //获取session工厂
        sf=conf.buildSessionFactory(); 
	}
	public static Session getSession(){		 
        //获取session实例
        return sf.openSession();
	}
}
