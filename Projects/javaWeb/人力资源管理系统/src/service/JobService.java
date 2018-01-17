package service;

import java.util.ArrayList;
import java.util.List;

import dao.JobDao;
import entity.Job;

public class JobService {
	private JobDao jobD=new JobDao();
	//应聘信息录入
	public boolean addJob(Job job){
		if(!jobD.ExistsJob(job)){
		   jobD.addJob(job);
		   System.out.println("添加"+job.getName()+"工作成功");
		   return  true;
		}
		return false;
	}
  //列举所有入库应聘信息
	public List<Job> listStockJob(){
		List<Job> list=jobD.listJob();
		List<Job>  list1=new ArrayList<Job>();
		for(Job job:list){
			if(job.getIsstock()==1){
				   list1.add(job);
			}
		}
		System.out.println("列举入库应聘信息成功");
		return list1;
	}
	//列举所有未入库应聘信息
	public List<Job> listUNStockJob(){
		List<Job> list=jobD.listJob();
		List<Job>  list1=new ArrayList<Job>();
		for(Job job:list){
			if(job.getIsstock()==0){
				   list1.add(job);
			}
		}
		System.out.println("列举未入库应聘信息成功");
		return list1;
	}
	//人员详细信息
	public Job detailJob(Long id){
		Job job=jobD.loadJob(id);
		System.out.println("显示"+job.getName()+"的详细信息");
		return job;
	}
	//人才信息删除
	public void deleteJob(Job job){
		jobD.deleteJob(job);
		System.out.println("删除人才信息成功");
	}
	//人员信息入库
	public Job stockJob(Long id){
		Job job=jobD.loadJob(id);
		jobD.Stock(job);
		System.out.println("入库"+job.getName());
		return job;
	}
}
