package action;

import java.util.HashMap;
import java.util.Map;

import service.SentenceService;

import com.opensymphony.xwork2.ActionSupport;
import com.opensymphony.xwork2.ModelDriven;

import entity.Sentence;

public class SentenceAction extends ActionSupport implements ModelDriven<Sentence>{
//	private Sentence sentence = new Sentence();
	private SentenceService service = new SentenceService();
	private Map<String,Object> sentenceMap = new HashMap<String,Object>();
	
	public Map<String, Object> getSentenceMap() {
		return sentenceMap;
	}
	public void setSentenceMap(Map<String, Object> sentenceMap) {
		this.sentenceMap = sentenceMap;
	}
	public String getSentence(){
		String sent= service.getSentence();
		sentenceMap.put("status", "1001");
		sentenceMap.put("data", sent);
		return "success";
	}
	@Override
	public Sentence getModel() {
		// TODO Auto-generated method stub
		return null;
	}
	
}
