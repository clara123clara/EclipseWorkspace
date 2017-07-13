
package com.lin.service;  
  
import org.apache.log4j.Logger;  
import org.junit.Test;  
import org.springframework.beans.factory.annotation.Autowired;  
  
import com.lin.baseTest.SpringTestCase;  
import com.jia.domain.user;  
  
/** 
 * 功能概要：UserService单元测试 
 *  
 * @author  
 * @since  2015年9月28日  
 */  
public class UserServiceTest extends SpringTestCase {  
    @Autowired  
    private UserService userService;  
    Logger logger = Logger.getLogger(UserServiceTest.class);  
      
    @Test  
    public void selectUserByIdTest(){  
        //user user = userService.selectUserById(10);  
    	user u = userService.selectUserByLoginNameAndPassword("evan", "123");
        logger.debug("查找结果" + u);  
    }  
      
  
}  