package action;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import service.NoticeService;
import util.MapUtil;
import util.actionUtil;

import com.opensymphony.xwork2.ActionSupport;
import com.opensymphony.xwork2.ModelDriven;

import entity.Job;
import entity.Notice;

public class NoticeAction extends ActionSupport  implements ModelDriven<Notice> {
   private  Notice  notice=new Notice();
   private Map<String,Object> NoticeAction= new HashMap<String, Object>();
   public Map<String, Object> getNoticeAction() {
	return NoticeAction;
}
private NoticeService ns=new NoticeService();
	
	//列举所有应聘信息
		public String listNotice(){
			actionUtil.kuayu();
			NoticeAction.clear();
			List<Notice> list=ns.listNotice();
			System.out.print(list.size());
			MapUtil.setStatus(NoticeAction, "1002");
			MapUtil.setOther(NoticeAction, list);
			MapUtil.setTotalNumber(NoticeAction, list.size());
			return "success";
		}
	@Override
	public Notice getModel() {
		// TODO 自动生成的方法存根
		return notice;
	}

}
