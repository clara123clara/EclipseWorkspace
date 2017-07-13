package com.jia.domain;
/** 
 * User映射类 
 * 对应数据库中表的字段
 *  
 * @author  jiajia
 * @time 2017
 */ 
public class User {
	 private Integer userId;  
	    private String userName;  
	    private String userPassword;  
	    private String userEmail;  
	  
	    public Integer getUserId() {  
	        return userId;  
	    }  
	  
	    public void setUserId(Integer userId) {  
	        this.userId = userId;  
	    }  
	  
	    public String getUserName() {  
	        return userName;  
	    }  
	  
	    public void setUserName(String userName) {  
	        this.userName = userName;  
	    }  
	  
	    public String getUserPassword() {  
	        return userPassword;  
	    }  
	  
	    public void setUserPassword(String userPassword) {  
	        this.userPassword = userPassword;  
	    }  
	  
	    public String getUserEmail() {  
	        return userEmail;  
	    }  
	  
	    public void setUserEmail(String userEmail) {  
	        this.userEmail = userEmail;  
	    }  
	  
	    @Override  
	    public String toString() {  
	        return "User [userId=用户ID" + userId + ", userName=用户名" + userName  
	                + ", userPassword=用户密码" + userPassword + ", userEmail=电子邮件" + userEmail  
	                + "]";  
	    }  

}
