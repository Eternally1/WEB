package action;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import service.DiaryService;
import util.DateUtil;

import com.opensymphony.xwork2.ActionSupport;
import com.opensymphony.xwork2.ModelDriven;

import entity.Diary;
import entity.DiarySend;

public class DiaryAction extends ActionSupport implements ModelDriven<Diary>{
	private Diary diary = new Diary();
	private DiaryService diaryService = new DiaryService();
	private Map<String,Object> diaryMap = new HashMap<String,Object>();
	/**
	 * 员工
	 * 输入：userID+strTime
	 * 员工自己查询
	 * 根据员工id+日期：查询该员工的本月的日志
	 * 以列表形式返回
	 * @param userID
	 * @return
	 */
	public String listDiarys_Month(){
		List<DiarySend> list = diaryService.listDiarys_Month(diary.getUserID(),diary.getStrTime());		
		diaryMap.put("status", "1001");
		diaryMap.put("data", list);
		return "success";	
	}
	/**
	 * 管理员
	 * 输入：strTime
	 * 根据日期：查询当天员工日志
	 * 以列表形式返回
	 * @param userID
	 * @return
	 */
	public String listDiarys_All(){
		List<DiarySend> list = diaryService.listDiarys_All(diary);			
		diaryMap.put("status", "1001");
		diaryMap.put("data", list);		
		return "success";	
	}
	/**
	 * 添加员工日志
	 * @return
	 */
	public String addDiary(){
		boolean flag = diaryService.addDiary(diary);
		String str = "";
		if(flag){
			//成功添加
			diaryMap.put("status", "1001");
			diaryMap.put("data", "添加日志成功");
			str = "success";
		}else{
			//已经存在
			diaryMap.put("status", "1002");
			diaryMap.put("data", "当天日志已经存在");
			str = "failed";
		}
		return str;
	}
	/**
	 * 修改日志
	 * @return
	 */
	public String updateDiary(){
		diaryService.updateDiary(diary);
		diaryMap.put("status", "1001");
		diaryMap.put("data", "日志修改成功");
		return "success";
	}
	/**
	 * 输入：userID+strTime
	 * 加载选定日期日志详细内容：id+日期。
	 * @return
	 */
	public String loadDiary(){		
		DiarySend dia = diaryService.loadDiary(diary.getUserID(),diary.getStrTime());
		if(dia == null){
			diaryMap.put("status", "1001");
			diaryMap.put("data", null);
		}else{
			diaryMap.put("status", "1001");
			diaryMap.put("data", dia);		
		}
		return "success";
	}
	
	public Map<String, Object> getDiaryMap() {
		return diaryMap;
	}
	public void setDiaryMap(Map<String, Object> diaryMap) {
		this.diaryMap = diaryMap;
	}
	@Override
	public Diary getModel() {
		// TODO Auto-generated method stub
		return diary;
	}

}
