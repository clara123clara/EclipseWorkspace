package com.jia.dao;

import com.jia.domain.User;
/** 
 * 功能概要：User的DAO类 
 *  
 *  Dao接口类，用来对应mapper文件
 * @author 
 * @since 
 */  
public interface userDao {
	public User selectUserById(Integer userId);  
	public User selectUserByLoginNameAndPassword(String userName,String password);
	public User selectUserByUserName(String userName);
}
