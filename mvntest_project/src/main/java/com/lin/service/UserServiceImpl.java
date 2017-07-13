package com.lin.service;  
  
import org.springframework.beans.factory.annotation.Autowired;  
import org.springframework.stereotype.Service;  
  
import com.jia.dao.userDao;
import com.jia.domain.User;  
  
/** 
 * 功能概要：UserService实现类 
 *  
 * @author  
 * @since  2015年9月28日  
 */  
@Service  
public class UserServiceImpl implements UserService{  
    @Autowired  
    private userDao userDao;  
  
    public User selectUserById(Integer userId) {  
        
        return userDao.selectUserById(userId);
          
    }

//	@Override
//	public user selectUserByLoginNameAndPassword(String userName,
//			String password) {
//		return userDao.selectUserByLoginNameAndPassword(userName, password);
//	}  
  
}  