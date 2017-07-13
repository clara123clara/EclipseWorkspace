
package com.lin.service;  
  
import com.jia.domain.User;
  
/** 
 * 功能概要：UserService接口类 
 *  
 *  service接口类
 * @author  
 * @since  2015年9月28日  
 */  
public interface UserService {  
	User selectUserById(Integer userId);  
    //public User selectUserByLoginNameAndPassword(String userName,String password);
}  